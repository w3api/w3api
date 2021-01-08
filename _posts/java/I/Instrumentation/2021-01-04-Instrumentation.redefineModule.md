---
title: Instrumentation.redefineModule()
permalink: Java/Instrumentation/redefineModule
date: 2021-01-04
key: JavaJava.I.Instrumentation
category: java
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
* **List&lt;Class&lt;?&gt;&gt;&gt; extraProvides**,  {% include w3api/param_description.html metodo=_data parametro="List<Class<?>>> extraProvides" %}
* **Module module**,  {% include w3api/param_description.html metodo=_data parametro="Module module" %}
* **Set&lt;Class&lt;?&gt;&gt; extraUses**,  {% include w3api/param_description.html metodo=_data parametro="Set<Class<?>> extraUses" %}
* **Set&lt;Module&gt;&gt; extraOpens**,  {% include w3api/param_description.html metodo=_data parametro="Set<Module>> extraOpens" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **Map&lt;Class&lt;?&gt;**,  {% include w3api/param_description.html metodo=_data parametro="Map<Class<?>" %}
* **Set&lt;Module&gt; extraReads**,  {% include w3api/param_description.html metodo=_data parametro="Set<Module> extraReads" %}
* **Set&lt;Module&gt;&gt; extraExports**,  {% include w3api/param_description.html metodo=_data parametro="Set<Module>> extraExports" %}

## Excepciones
[UnmodifiableModuleException](/Java/UnmodifiableModuleException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Instrumentation](/Java/Instrumentation/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Instrumentation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
