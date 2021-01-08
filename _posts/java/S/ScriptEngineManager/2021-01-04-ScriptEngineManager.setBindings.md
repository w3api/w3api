---
title: ScriptEngineManager.setBindings()
permalink: Java/ScriptEngineManager/setBindings
date: 2021-01-04
key: JavaJava.S.ScriptEngineManager
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineManager.metodos valor="setBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setBindings(Bindings bindings)
~~~

## Parámetros
* **Bindings bindings**,  {% include w3api/param_description.html metodo=_data parametro="Bindings bindings" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScriptEngineManager](/Java/ScriptEngineManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScriptEngineManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
