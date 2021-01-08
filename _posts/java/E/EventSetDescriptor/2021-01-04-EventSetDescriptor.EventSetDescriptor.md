---
title: EventSetDescriptor.EventSetDescriptor()
permalink: Java/EventSetDescriptor/EventSetDescriptor
date: 2021-01-04
key: JavaJava.E.EventSetDescriptor
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventSetDescriptor.constructores valor="EventSetDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String listenerMethodName) throws IntrospectionException
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String[] listenerMethodNames, String addListenerMethodName, String removeListenerMethodName) throws IntrospectionException
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String[] listenerMethodNames, String addListenerMethodName, String removeListenerMethodName, String getListenerMethodName) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, MethodDescriptor[] listenerMethodDescriptors, Method addListenerMethod, Method removeListenerMethod) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, Method[] listenerMethods, Method addListenerMethod, Method removeListenerMethod) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, Method[] listenerMethods, Method addListenerMethod, Method removeListenerMethod, Method getListenerMethod) throws IntrospectionException
~~~

## Parámetros
* **Method[] listenerMethods**,  {% include w3api/param_description.html metodo=_data parametro="Method[] listenerMethods" %}
* **Class&lt;?&gt; listenerType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> listenerType" %}
* **String[] listenerMethodNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] listenerMethodNames" %}
* **String removeListenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String removeListenerMethodName" %}
* **String getListenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String getListenerMethodName" %}
* **Method addListenerMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method addListenerMethod" %}
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String listenerMethodName" %}
* **String addListenerMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String addListenerMethodName" %}
* **Method removeListenerMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method removeListenerMethod" %}
* **MethodDescriptor[] listenerMethodDescriptors**,  {% include w3api/param_description.html metodo=_data parametro="MethodDescriptor[] listenerMethodDescriptors" %}
* **String eventSetName**,  {% include w3api/param_description.html metodo=_data parametro="String eventSetName" %}
* **Class&lt;?&gt; sourceClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> sourceClass" %}
* **Method getListenerMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method getListenerMethod" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[EventSetDescriptor](/Java/EventSetDescriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventSetDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
