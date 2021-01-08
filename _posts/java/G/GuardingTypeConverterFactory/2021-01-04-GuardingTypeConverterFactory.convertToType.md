---
title: GuardingTypeConverterFactory.convertToType()
permalink: Java/GuardingTypeConverterFactory/convertToType
date: 2021-01-04
key: JavaJava.G.GuardingTypeConverterFactory
category: java
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
* **Class&lt;?&gt; sourceType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> sourceType" %}
* **Class&lt;?&gt; targetType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> targetType" %}
* **Supplier&lt;MethodHandles.Lookup&gt; lookupSupplier**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<MethodHandles.Lookup> lookupSupplier" %}

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
{%- for _ldc in site.data.Java.G.GuardingTypeConverterFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
