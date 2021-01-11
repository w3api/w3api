---
title: SSLSessionBindingEvent.SSLSessionBindingEvent()
permalink: Java/SSLSessionBindingEvent/SSLSessionBindingEvent
date: 2021-01-11
key: JavaJava.S.SSLSessionBindingEvent
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSessionBindingEvent.constructores valor="SSLSessionBindingEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SSLSessionBindingEvent(SSLSession session, String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **SSLSession session**,  {% include w3api/param_description.html metodo=_dato parametro="SSLSession session" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLSessionBindingEvent](/Java/SSLSessionBindingEvent/)

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
