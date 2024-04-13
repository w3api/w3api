---
title: EventDirContext.addNamingListener()
permalink: /Java/EventDirContext/addNamingListener/
date: 2021-01-11
key: Java.E.EventDirContext
category: Java
tags: ['java se', 'javax.naming.event', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventDirContext.metodos valor="addNamingListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNamingListener(String target, String filter, Object[] filterArgs, SearchControls ctls, NamingListener l) throws NamingException
void addNamingListener(String target, String filter, SearchControls ctls, NamingListener l) throws NamingException
void addNamingListener(Name target, String filter, Object[] filterArgs, SearchControls ctls, NamingListener l) throws NamingException
void addNamingListener(Name target, String filter, SearchControls ctls, NamingListener l) throws NamingException
~~~

## Parámetros
* **NamingListener l**,  {% include w3api/param_description.html metodo=_dato parametro="NamingListener l" %}
* **Object[] filterArgs**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] filterArgs" %}
* **Name target**,  {% include w3api/param_description.html metodo=_dato parametro="Name target" %}
* **SearchControls ctls**,  {% include w3api/param_description.html metodo=_dato parametro="SearchControls ctls" %}
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}
* **String filter**,  {% include w3api/param_description.html metodo=_dato parametro="String filter" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[EventDirContext](/Java/EventDirContext/)

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
