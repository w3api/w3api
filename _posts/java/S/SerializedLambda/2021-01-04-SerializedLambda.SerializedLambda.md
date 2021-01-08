---
title: SerializedLambda.SerializedLambda()
permalink: Java/SerializedLambda/SerializedLambda
date: 2021-01-04
key: JavaJava.S.SerializedLambda
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerializedLambda.constructores valor="SerializedLambda" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerializedLambda(Class<?> capturingClass, String functionalInterfaceClass, String functionalInterfaceMethodName, String functionalInterfaceMethodSignature, int implMethodKind, String implClass, String implMethodName, String implMethodSignature, String instantiatedMethodType, Object[] capturedArgs)
~~~

## Parámetros
* **int implMethodKind**,  {% include w3api/param_description.html metodo=_data parametro="int implMethodKind" %}
* **String implMethodSignature**,  {% include w3api/param_description.html metodo=_data parametro="String implMethodSignature" %}
* **Class&lt;?&gt; capturingClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> capturingClass" %}
* **String functionalInterfaceMethodSignature**,  {% include w3api/param_description.html metodo=_data parametro="String functionalInterfaceMethodSignature" %}
* **String implMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String implMethodName" %}
* **String functionalInterfaceClass**,  {% include w3api/param_description.html metodo=_data parametro="String functionalInterfaceClass" %}
* **String implClass**,  {% include w3api/param_description.html metodo=_data parametro="String implClass" %}
* **String functionalInterfaceMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String functionalInterfaceMethodName" %}
* **String instantiatedMethodType**,  {% include w3api/param_description.html metodo=_data parametro="String instantiatedMethodType" %}
* **Object[] capturedArgs**,  {% include w3api/param_description.html metodo=_data parametro="Object[] capturedArgs" %}

## Clase Padre
[SerializedLambda](/Java/SerializedLambda/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SerializedLambda.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
