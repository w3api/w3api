---
title: ConnectionEventListener.connectionErrorOccurred()
permalink: /Java/ConnectionEventListener/connectionErrorOccurred/
date: 2021-01-11
key: Java.C.ConnectionEventListener
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConnectionEventListener.metodos valor="connectionErrorOccurred" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void connectionErrorOccurred(ConnectionEvent event)
~~~

## Parámetros
* **ConnectionEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="ConnectionEvent event" %}

## Clase Padre
[ConnectionEventListener](/Java/ConnectionEventListener/)

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
