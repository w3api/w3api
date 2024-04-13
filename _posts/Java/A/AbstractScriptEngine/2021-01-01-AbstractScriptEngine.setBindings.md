---
title: AbstractScriptEngine.setBindings()
permalink: /Java/AbstractScriptEngine/setBindings/
date: 2021-01-11
key: Java.A.AbstractScriptEngine
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractScriptEngine.metodos valor="setBindings" %}

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
[AbstractScriptEngine](/Java/AbstractScriptEngine/)

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
