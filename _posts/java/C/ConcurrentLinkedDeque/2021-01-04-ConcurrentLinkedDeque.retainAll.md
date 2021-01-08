---
title: ConcurrentLinkedDeque.retainAll()
permalink: Java/ConcurrentLinkedDeque/retainAll
date: 2021-01-04
key: JavaJava.C.ConcurrentLinkedDeque
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedDeque.metodos valor="retainAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean retainAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<?> c" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentLinkedDeque](/Java/ConcurrentLinkedDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentLinkedDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
