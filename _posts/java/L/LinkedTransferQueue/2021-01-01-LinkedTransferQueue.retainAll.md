---
title: LinkedTransferQueue.retainAll()
permalink: /Java/LinkedTransferQueue/retainAll/
date: 2021-01-11
key: Java.L.LinkedTransferQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedTransferQueue.metodos valor="retainAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean retainAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedTransferQueue](/Java/LinkedTransferQueue/)

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
