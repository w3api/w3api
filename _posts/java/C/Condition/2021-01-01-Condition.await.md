---
title: Condition.await()
permalink: Java/Condition/await
date: 2021-01-11
key: JavaJava.C.Condition
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Condition.metodos valor="await" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void await() throws InterruptedException
boolean await(long time, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long time**,  {% include w3api/param_description.html metodo=_dato parametro="long time" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[Condition](/Java/Condition/)

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
