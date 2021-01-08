---
title: CompositeName.CompositeName()
permalink: Java/CompositeName/CompositeName
date: 2021-01-04
key: JavaJava.C.CompositeName
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeName.constructores valor="CompositeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeName()
public CompositeName(String n) throws InvalidNameException
protected CompositeName(Enumeration<String> comps)
~~~

## Parámetros
* **String n**,  {% include w3api/param_description.html metodo=_data parametro="String n" %}
* **Enumeration&lt;String&gt; comps**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<String> comps" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/)

## Clase Padre
[CompositeName](/Java/CompositeName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
