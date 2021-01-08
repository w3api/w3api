---
title: Invocable.invokeMethod()
permalink: Java/Invocable/invokeMethod
date: 2021-01-04
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
* **Object thiz**,  {% include w3api/param_description.html metodo=_data parametro="Object thiz" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_data parametro="Object... args" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [NoSuchMethodException](/Java/NoSuchMethodException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Invocable](/Java/Invocable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Invocable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
