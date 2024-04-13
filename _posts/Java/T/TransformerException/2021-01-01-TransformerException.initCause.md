---
title: TransformerException.initCause()
permalink: /Java/TransformerException/initCause/
date: 2021-01-11
key: Java.T.TransformerException
category: Java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerException.metodos valor="initCause" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Throwable initCause(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[TransformerException](/Java/TransformerException/)

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
