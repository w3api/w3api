---
title: Instrumentation.redefineModule()
permalink: /Java/Instrumentation/redefineModule/
date: 2021-01-11
key: Java.I.Instrumentation
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="redefineModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void redefineModule(Module module, Set<Module> extraReads, Map<String,Set<Module>> extraExports, Map<String,Set<Module>> extraOpens, Set<Class<?>> extraUses, Map<Class<?>,List<Class<?>>> extraProvides)
~~~

## Parámetros
* **Set&lt;Module&gt;&gt; extraExports**,  {% include w3api/param_description.html metodo=_dato parametro="Set<Module>> extraExports" %}
* **Module module**,  {% include w3api/param_description.html metodo=_dato parametro="Module module" %}
* **Set&lt;Module&gt; extraReads**,  {% include w3api/param_description.html metodo=_dato parametro="Set<Module> extraReads" %}
* **List&lt;Class&lt;?&gt;&gt;&gt; extraProvides**,  {% include w3api/param_description.html metodo=_dato parametro="List<Class<?>>> extraProvides" %}
* **Set&lt;Class&lt;?&gt;&gt; extraUses**,  {% include w3api/param_description.html metodo=_dato parametro="Set<Class<?>> extraUses" %}
* **Set&lt;Module&gt;&gt; extraOpens**,  {% include w3api/param_description.html metodo=_dato parametro="Set<Module>> extraOpens" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **Map&lt;Class&lt;?&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Map<Class<?>" %}

## Excepciones
[UnmodifiableModuleException](/Java/UnmodifiableModuleException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Instrumentation](/Java/Instrumentation/)

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
