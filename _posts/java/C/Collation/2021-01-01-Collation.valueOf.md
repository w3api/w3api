---
title: Collation.valueOf()
permalink: /Java/Collation/valueOf/
date: 2021-01-11
key: Java.C.Collation
category: Java
tags: ['java se', 'javafx.print', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collation.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Collation valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Collation](/Java/Collation/)

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
