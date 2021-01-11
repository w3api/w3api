---
title: DirContext.getAttributes()
permalink: Java/DirContext/getAttributes
date: 2021-01-11
key: JavaJava.D.DirContext
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirContext.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Attributes getAttributes(String name) throws NamingException
Attributes getAttributes(String name, String[] attrIds) throws NamingException
Attributes getAttributes(Name name) throws NamingException
Attributes getAttributes(Name name, String[] attrIds) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **String[] attrIds**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attrIds" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[DirContext](/Java/DirContext/)

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
