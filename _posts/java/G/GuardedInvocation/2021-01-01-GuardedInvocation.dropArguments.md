---
title: GuardedInvocation.dropArguments()
permalink: Java/GuardedInvocation/dropArguments
date: 2021-01-11
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
* **Class&lt;?&gt;... valueTypes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>... valueTypes" %}
* **List&lt;Class&lt;?&gt;&gt; valueTypes**,  {% include w3api/param_description.html metodo=_dato parametro="List<Class<?>> valueTypes" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Clase Padre
[GuardedInvocation](/Java/GuardedInvocation/)

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
