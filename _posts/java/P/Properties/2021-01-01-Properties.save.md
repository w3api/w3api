---
title: Properties.save()
permalink: Java/Properties/save
date: 2021-01-11
key: JavaJava.P.Properties
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="save" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public void save(OutputStream out, String comments)
~~~

## Parámetros
* **String comments**,  {% include w3api/param_description.html metodo=_dato parametro="String comments" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[Properties](/Java/Properties/)

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
