---
title: CompoundName.add()
permalink: Java/CompoundName/add
date: 2021-01-04
key: JavaJava.C.CompoundName
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompoundName.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Name add(int posn, String comp) throws InvalidNameException
public Name add(String comp) throws InvalidNameException
~~~

## Parámetros
* **int posn**,  {% include w3api/param_description.html metodo=_data parametro="int posn" %}
* **String comp**,  {% include w3api/param_description.html metodo=_data parametro="String comp" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [InvalidNameException](/Java/InvalidNameException/)

## Clase Padre
[CompoundName](/Java/CompoundName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompoundName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
