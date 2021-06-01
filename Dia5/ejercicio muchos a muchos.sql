# visualizar todos los alumnos con sus cursos
select  *
from alumnos 
inner join alumnos_cursos 
on id = alumnos_cursos.alumnos_id
inner join cursos
on alumnos_cursos.cursos_id = cursos.id;

#1. Los cursos con su cantidad de alumnos
select nombre,count(*) 'cantidad de alumnos'
from cursos as c
inner join alumnos_cursos as ac
on c.id = ac.cursos_id
group by nombre;

#2. El alumno con mas cursos matriculados
#el metodo concat_ws funciona de la sgte manera
#3 parametros como minimo en el cual el 1er parametro sera para indicar cual es el separador entre
#columna y columna, y luego los demas parametros sirven para concatenar
select concat_ws(' ',matricula,nombre,apellido) as 'ALUMNO',count(matricula) 'CURSOS MATRICULADOS'
from alumnos as a
inner join alumnos_cursos as ac 
on a.id = ac.alumnos_id
group by concat_ws(' ',matricula,nombre,apellido)
having count(*)=(
	select count(*)
    from alumnos as a
	inner join alumnos_cursos as ac 
    on a.id = ac.alumnos_id
    group by nombre, apellido
    order by 1 desc
    limit 1
) -- el having se usa para filtro pero con funciones de agregacion
order by count(matricula)desc;

#3 el alumno mas viejo y sus cursos
select *
from alumnos
inner join alumnos_cursos
on alumnos.id = alumnos_cursos.alumnos_id
inner join cursos
on alumnos_cursos.cursos_id = cursos.id
group by alumnos.id
order by fecha_nacimiento asc
limit 1;

#4. los cursos que empezaron entre el 01 de mayo y el 01 de junio
select *
from cursos
where fecha_inicio between "2021-05-01" and  "2021-06-01";
