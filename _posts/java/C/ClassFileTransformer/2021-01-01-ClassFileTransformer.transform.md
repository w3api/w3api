---
title: ClassFileTransformer.transform()
permalink: /Java/ClassFileTransformer/transform/
date: 2021-01-11
key: Java.C.ClassFileTransformer
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassFileTransformer.metodos valor="transform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default byte[] transform(ClassLoader loader, String className, Class<?> classBeingRedefined, ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException
default byte[] transform(Module module, ClassLoader loader, String className, Class<?> classBeingRedefined, ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **Class&lt;?&gt; classBeingRedefined**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> classBeingRedefined" %}
* **ProtectionDomain protectionDomain**,  {% include w3api/param_description.html metodo=_dato parametro="ProtectionDomain protectionDomain" %}
* **Module module**,  {% include w3api/param_description.html metodo=_dato parametro="Module module" %}
* **byte[] classfileBuffer**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] classfileBuffer" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[IllegalClassFormatException](/Java/IllegalClassFormatException/)

## Clase Padre
[ClassFileTransformer](/Java/ClassFileTransformer/)

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
