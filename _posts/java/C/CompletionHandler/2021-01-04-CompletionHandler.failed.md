---
title: CompletionHandler.failed()
permalink: Java/CompletionHandler/failed
date: 2021-01-04
key: JavaJava.C.CompletionHandler
category: java
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
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **Throwable exc**,  {% include w3api/param_description.html metodo=_data parametro="Throwable exc" %}

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
