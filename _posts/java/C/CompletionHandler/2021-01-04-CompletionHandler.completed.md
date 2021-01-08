---
title: CompletionHandler.completed()
permalink: Java/CompletionHandler/completed
date: 2021-01-04
key: JavaJava.C.CompletionHandler
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionHandler.metodos valor="completed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void completed(V result, A attachment)
~~~

## Parámetros
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **V result**,  {% include w3api/param_description.html metodo=_data parametro="V result" %}

## Clase Padre
[CompletionHandler](/Java/CompletionHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
