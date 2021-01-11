---
title: Properties.store()
permalink: Java/Properties/store
date: 2021-01-11
key: JavaJava.P.Properties
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="store" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void store(OutputStream out, String comments) throws IOException
public void store(Writer writer, String comments) throws IOException
~~~

## Parámetros
* **String comments**,  {% include w3api/param_description.html metodo=_dato parametro="String comments" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_dato parametro="Writer writer" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [IOException](/Java/IOException/)

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
