---
title: GuardingTypeConverterFactory.convertToType()
permalink: /Java/GuardingTypeConverterFactory/convertToType/
date: 2021-01-11
key: Java.G.GuardingTypeConverterFactory
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardingTypeConverterFactory.metodos valor="convertToType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
GuardedInvocation convertToType(Class<?> sourceType, Class<?> targetType, Supplier<MethodHandles.Lookup> lookupSupplier) throws Exception
~~~

## Parámetros
* **Supplier&lt;MethodHandles.Lookup&gt; lookupSupplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<MethodHandles.Lookup> lookupSupplier" %}
* **Class&lt;?&gt; sourceType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> sourceType" %}
* **Class&lt;?&gt; targetType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> targetType" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[GuardingTypeConverterFactory](/Java/GuardingTypeConverterFactory/)

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
