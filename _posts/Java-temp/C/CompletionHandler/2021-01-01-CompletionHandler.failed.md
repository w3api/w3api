---
title: CompletionHandler.failed()
permalink: /Java/CompletionHandler/failed/
date: 2021-01-11
key: Java.C.CompletionHandler
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionHandler.metodos valor="failed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void failed(Throwable exc, A attachment)
~~~

## Parámetros
* **Throwable exc**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exc" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}

## Clase Padre
[CompletionHandler](/Java/CompletionHandler/)

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
