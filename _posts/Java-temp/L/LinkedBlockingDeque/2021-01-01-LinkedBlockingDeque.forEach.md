---
title: LinkedBlockingDeque.forEach()
permalink: /Java/LinkedBlockingDeque/forEach/
date: 2021-01-11
key: Java.L.LinkedBlockingDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedBlockingDeque.metodos valor="forEach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEach(Consumer<? super E> action)
~~~

## Parámetros
* **Consumer&lt;? super E&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super E> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedBlockingDeque](/Java/LinkedBlockingDeque/)

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
