---
title: SerializedLambda.SerializedLambda()
permalink: /Java/SerializedLambda/SerializedLambda/
date: 2021-01-11
key: Java.S.SerializedLambda
category: Java
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
* **Object[] capturedArgs**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] capturedArgs" %}
* **String functionalInterfaceMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String functionalInterfaceMethodName" %}
* **Class&lt;?&gt; capturingClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> capturingClass" %}
* **String functionalInterfaceClass**,  {% include w3api/param_description.html metodo=_dato parametro="String functionalInterfaceClass" %}
* **int implMethodKind**,  {% include w3api/param_description.html metodo=_dato parametro="int implMethodKind" %}
* **String implMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String implMethodName" %}
* **String functionalInterfaceMethodSignature**,  {% include w3api/param_description.html metodo=_dato parametro="String functionalInterfaceMethodSignature" %}
* **String implClass**,  {% include w3api/param_description.html metodo=_dato parametro="String implClass" %}
* **String implMethodSignature**,  {% include w3api/param_description.html metodo=_dato parametro="String implMethodSignature" %}
* **String instantiatedMethodType**,  {% include w3api/param_description.html metodo=_dato parametro="String instantiatedMethodType" %}

## Clase Padre
[SerializedLambda](/Java/SerializedLambda/)

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
