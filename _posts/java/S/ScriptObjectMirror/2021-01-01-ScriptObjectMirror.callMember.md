---
title: ScriptObjectMirror.callMember()
permalink: Java/ScriptObjectMirror/callMember
date: 2021-01-11
key: JavaJava.S.ScriptObjectMirror
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptObjectMirror.metodos valor="callMember" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object callMember(String functionName, Object... args)
~~~

## Parámetros
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}
* **String functionName**,  {% include w3api/param_description.html metodo=_dato parametro="String functionName" %}

## Clase Padre
[ScriptObjectMirror](/Java/ScriptObjectMirror/)

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
