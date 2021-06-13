---
title: NamingEvent.NamingEvent()
permalink: Java/NamingEvent/NamingEvent
date: 2021-01-11
key: JavaJava.N.NamingEvent
category: Java
tags: ['java se', 'javax.naming.event', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingEvent.constructores valor="NamingEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NamingEvent(EventContext source, int type, Binding newBd, Binding oldBd, Object changeInfo)
~~~

## Parámetros
* **EventContext source**,  {% include w3api/param_description.html metodo=_dato parametro="EventContext source" %}
* **Binding oldBd**,  {% include w3api/param_description.html metodo=_dato parametro="Binding oldBd" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **Object changeInfo**,  {% include w3api/param_description.html metodo=_dato parametro="Object changeInfo" %}
* **Binding newBd**,  {% include w3api/param_description.html metodo=_dato parametro="Binding newBd" %}

## Clase Padre
[NamingEvent](/Java/NamingEvent/)

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
