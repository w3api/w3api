---
title: Properties.store()
permalink: Java/Properties/store
date: 2021-01-04
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
* **Writer writer**,  {% include w3api/param_description.html metodo=_data parametro="Writer writer" %}
* **String comments**,  {% include w3api/param_description.html metodo=_data parametro="String comments" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Properties.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
