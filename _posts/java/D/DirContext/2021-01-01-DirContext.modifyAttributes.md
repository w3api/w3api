---
title: DirContext.modifyAttributes()
permalink: Java/DirContext/modifyAttributes
date: 2021-01-11
key: JavaJava.D.DirContext
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirContext.metodos valor="modifyAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void modifyAttributes(String name, int mod_op, Attributes attrs) throws NamingException
void modifyAttributes(String name, ModificationItem[] mods) throws NamingException
void modifyAttributes(Name name, int mod_op, Attributes attrs) throws NamingException
void modifyAttributes(Name name, ModificationItem[] mods) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int mod_op**,  {% include w3api/param_description.html metodo=_dato parametro="int mod_op" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes attrs" %}
* **ModificationItem[] mods**,  {% include w3api/param_description.html metodo=_dato parametro="ModificationItem[] mods" %}

## Excepciones
[AttributeModificationException](/Java/AttributeModificationException/), [NamingException](/Java/NamingException/)

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
