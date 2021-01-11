---
title: SocketImpl.setPerformancePreferences()
permalink: Java/SocketImpl/setPerformancePreferences
date: 2021-01-11
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="setPerformancePreferences" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void setPerformancePreferences(int connectionTime, int latency, int bandwidth)
~~~

## Parámetros
* **int bandwidth**,  {% include w3api/param_description.html metodo=_dato parametro="int bandwidth" %}
* **int connectionTime**,  {% include w3api/param_description.html metodo=_dato parametro="int connectionTime" %}
* **int latency**,  {% include w3api/param_description.html metodo=_dato parametro="int latency" %}

## Clase Padre
[SocketImpl](/Java/SocketImpl/)

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
