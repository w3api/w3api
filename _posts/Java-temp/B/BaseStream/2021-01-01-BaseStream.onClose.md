---
title: BaseStream.onClose()
permalink: /Java/BaseStream/onClose/
date: 2021-01-11
key: Java.B.BaseStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseStream.metodos valor="onClose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
S onClose(Runnable closeHandler)
~~~

## Parámetros
* **Runnable closeHandler**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable closeHandler" %}

## Clase Padre
[BaseStream](/Java/BaseStream/)

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
