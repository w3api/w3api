---
title: AbstractQueuedSynchronizer.tryReleaseShared()
permalink: /Java/AbstractQueuedSynchronizer/tryReleaseShared/
date: 2021-01-11
key: Java.A.AbstractQueuedSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedSynchronizer.metodos valor="tryReleaseShared" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean tryReleaseShared(int arg)
~~~

## Parámetros
* **int arg**,  {% include w3api/param_description.html metodo=_dato parametro="int arg" %}

## Excepciones
[IllegalMonitorStateException](/Java/IllegalMonitorStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[AbstractQueuedSynchronizer](/Java/AbstractQueuedSynchronizer/)

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
