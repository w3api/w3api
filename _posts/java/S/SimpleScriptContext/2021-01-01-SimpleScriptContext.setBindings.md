---
title: SimpleScriptContext.setBindings()
permalink: Java/SimpleScriptContext/setBindings
date: 2021-01-11
key: JavaJava.S.SimpleScriptContext
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleScriptContext.metodos valor="setBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setBindings(Bindings bindings, int scope)
~~~

## Parámetros
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}
* **Bindings bindings**,  {% include w3api/param_description.html metodo=_dato parametro="Bindings bindings" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
