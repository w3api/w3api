---
title: Invocable.invokeMethod()
permalink: Java/Invocable/invokeMethod
date: 2021-01-11
key: JavaJava.I.Invocable
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Invocable.metodos valor="invokeMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invokeMethod(Object thiz, String name, Object... args) throws ScriptException, NoSuchMethodException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object thiz**,  {% include w3api/param_description.html metodo=_dato parametro="Object thiz" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NoSuchMethodException](/Java/NoSuchMethodException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Invocable](/Java/Invocable/)

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
