---
title: GuardedInvocation.dropArguments()
permalink: Java/GuardedInvocation/dropArguments
date: 2021-01-04
key: JavaJava.G.GuardedInvocation
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.metodos valor="dropArguments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation dropArguments(int pos, Class<?>... valueTypes)
public GuardedInvocation dropArguments(int pos, List<Class<?>> valueTypes)
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Class&lt;?&gt;... valueTypes**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>... valueTypes" %}
* **List&lt;Class&lt;?&gt;&gt; valueTypes**,  {% include w3api/param_description.html metodo=_data parametro="List<Class<?>> valueTypes" %}

## Clase Padre
[GuardedInvocation](/Java/GuardedInvocation/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GuardedInvocation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
