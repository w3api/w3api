---
title: InitialDirContext.InitialDirContext()
permalink: /Java/InitialDirContext/InitialDirContext/
date: 2021-01-11
key: Java.I.InitialDirContext
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialDirContext.constructores valor="InitialDirContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InitialDirContext() throws NamingException
protected InitialDirContext(boolean lazy) throws NamingException
public InitialDirContext(Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **boolean lazy**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lazy" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialDirContext](/Java/InitialDirContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
