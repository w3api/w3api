---
title: EventContext.addNamingListener()
permalink: /Java/EventContext/addNamingListener/
date: 2021-01-11
key: Java.E.EventContext
category: Java
tags: ['java se', 'javax.naming.event', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventContext.metodos valor="addNamingListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNamingListener(String target, int scope, NamingListener l) throws NamingException
void addNamingListener(Name target, int scope, NamingListener l) throws NamingException
~~~

## Parámetros
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}
* **NamingListener l**,  {% include w3api/param_description.html metodo=_dato parametro="NamingListener l" %}
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}
* **Name target**,  {% include w3api/param_description.html metodo=_dato parametro="Name target" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[EventContext](/Java/EventContext/)

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
