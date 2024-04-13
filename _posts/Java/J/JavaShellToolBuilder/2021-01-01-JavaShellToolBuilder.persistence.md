---
title: JavaShellToolBuilder.persistence()
permalink: /Java/JavaShellToolBuilder/persistence/
date: 2021-01-11
key: Java.J.JavaShellToolBuilder
category: Java
tags: ['java se', 'jdk.jshell.tool', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaShellToolBuilder.metodos valor="persistence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaShellToolBuilder persistence(Map<String,String> prefsMap)
JavaShellToolBuilder persistence(Preferences prefs)
~~~

## Parámetros
* **String&gt; prefsMap**,  {% include w3api/param_description.html metodo=_dato parametro="String> prefsMap" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **Preferences prefs**,  {% include w3api/param_description.html metodo=_dato parametro="Preferences prefs" %}

## Clase Padre
[JavaShellToolBuilder](/Java/JavaShellToolBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
