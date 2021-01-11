---
title: InitialContext.InitialContext()
permalink: Java/InitialContext/InitialContext
date: 2021-01-11
key: JavaJava.I.InitialContext
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3', 'JNDI Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContext.constructores valor="InitialContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InitialContext() throws NamingException
protected InitialContext(boolean lazy) throws NamingException
public InitialContext(Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **boolean lazy**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lazy" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialContext](/Java/InitialContext/)

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
