---
title: AsyncHandler.handleResponse()
permalink: /Java/AsyncHandler/handleResponse/
date: 2021-01-11
key: Java.A.AsyncHandler
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsyncHandler.metodos valor="handleResponse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void handleResponse(Response<T> res)
~~~

## Parámetros
* **Response&lt;T&gt; res**,  {% include w3api/param_description.html metodo=_dato parametro="Response<T> res" %}

## Clase Padre
[AsyncHandler](/Java/AsyncHandler/)

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
