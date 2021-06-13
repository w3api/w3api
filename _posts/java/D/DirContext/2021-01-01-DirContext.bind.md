---
title: DirContext.bind()
permalink: /Java/DirContext/bind/
date: 2021-01-11
key: Java.D.DirContext
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirContext.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void bind(String name, Object obj, Attributes attrs) throws NamingException
void bind(Name name, Object obj, Attributes attrs) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes attrs" %}

## Excepciones
[NameAlreadyBoundException](/Java/NameAlreadyBoundException/), [InvalidAttributesException](/Java/InvalidAttributesException/), [NamingException](/Java/NamingException/)

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
