---
title: DirContext.modifyAttributes()
permalink: Java/DirContext/modifyAttributes
date: 2021-01-04
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
* **int mod_op**,  {% include w3api/param_description.html metodo=_data parametro="int mod_op" %}
* **ModificationItem[] mods**,  {% include w3api/param_description.html metodo=_data parametro="ModificationItem[] mods" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_data parametro="Attributes attrs" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

## Excepciones
[NamingException](/Java/NamingException/), [AttributeModificationException](/Java/AttributeModificationException/)

## Clase Padre
[DirContext](/Java/DirContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
