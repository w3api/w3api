---
title: CompoundName.remove()
permalink: /Java/CompoundName/remove/
date: 2021-01-11
key: Java.C.CompoundName
category: Java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompoundName.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object remove(int posn) throws InvalidNameException
~~~

## Parámetros
* **int posn**,  {% include w3api/param_description.html metodo=_dato parametro="int posn" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[CompoundName](/Java/CompoundName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
