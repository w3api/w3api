---
title: InitialDirContext.InitialDirContext()
permalink: Java/InitialDirContext/InitialDirContext
date: 2021-01-04
key: JavaJava.I.InitialDirContext
category: java
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
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}
* **boolean lazy**,  {% include w3api/param_description.html metodo=_data parametro="boolean lazy" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialDirContext](/Java/InitialDirContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InitialDirContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
