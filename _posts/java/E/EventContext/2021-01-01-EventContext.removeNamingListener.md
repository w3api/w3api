---
title: EventContext.removeNamingListener()
permalink: Java/EventContext/removeNamingListener
date: 2021-01-11
key: JavaJava.E.EventContext
category: java
tags: ['java se', 'javax.naming.event', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventContext.metodos valor="removeNamingListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNamingListener(NamingListener l) throws NamingException
~~~

## Parámetros
* **NamingListener l**,  {% include w3api/param_description.html metodo=_dato parametro="NamingListener l" %}

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
