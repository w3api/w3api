---
title: SimpleScriptContext.getBindings()
permalink: /Java/SimpleScriptContext/getBindings/
date: 2021-01-11
key: Java.S.SimpleScriptContext
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleScriptContext.metodos valor="getBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Bindings getBindings(int scope)
~~~

## Parámetros
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SimpleScriptContext](/Java/SimpleScriptContext/)

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
