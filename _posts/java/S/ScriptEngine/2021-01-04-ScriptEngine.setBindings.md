---
title: ScriptEngine.setBindings()
permalink: Java/ScriptEngine/setBindings
date: 2021-01-04
key: JavaJava.S.ScriptEngine
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngine.metodos valor="setBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setBindings(Bindings bindings, int scope)
~~~

## Parámetros
* **Bindings bindings**,  {% include w3api/param_description.html metodo=_data parametro="Bindings bindings" %}
* **int scope**,  {% include w3api/param_description.html metodo=_data parametro="int scope" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScriptEngine](/Java/ScriptEngine/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScriptEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
