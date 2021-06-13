---
title: ObjectName.unquote()
permalink: /Java/ObjectName/unquote/
date: 2021-01-11
key: JavaJava.O.ObjectName
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectName.metodos valor="unquote" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String unquote(String q)
~~~

## Parámetros
* **String q**,  {% include w3api/param_description.html metodo=_dato parametro="String q" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObjectName](/Java/ObjectName/)

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
